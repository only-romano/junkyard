const CSSParsing = (cssText, customClasses)=> {
    /*
        cssText - user's input (css rules)
        customClasses - replacers for body and all rules - length = 2
    */
    let [ css, l_ind, selector ] = [ "", 0, "" ];
    let [ bodyClass, flagClass ] = customClasses;
    cssText = cssText.split('}');

    for (let i = 0 ; i < cssText.length; i++) {
    // Перебор неизменяемых CSS-правил для правки селекторов.
        cssText[i] = cssText[i].replace(/body/gi, bodyClass);
        l_ind = cssText[i].indexOf('{');
        if (~l_ind && cssText[i].indexOf(':')) {
            selector = CSSReplaceId(cssText[i]
                .slice(0, l_ind))
                    .replace(/,/gi, ', ' + flagClass + ' ');

            if (selector.replace(/ /gi, '').indexOf('@') == 0)
                css += selector + cssText[i].slice(l_ind) + "} ";
            else
                css += flagClass + " " + selector + cssText[i].slice(l_ind) + "} ";
        }
    }
    
    // innerHTML for style element
    return css;
}


const CSSReplaceId = (selector) => {
    let index = selector.indexOf('#');
    if (~index) {
        if (index == 0)
            selector = '[data-id="' + selector.slice(1);
        else
            selector = selector.slice(0, index) + '[data-id="' +
                        selector.slice(index+1);

        let space = selector.slice(index).indexOf(' ');
        let dot = selector.slice(index).indexOf('.');
        let separator = selector.slice(index).indexOf(',');

        if ( ~space || ~dot || ~separator ) {
            space = space == -1 ? 100 : space;
            dot = dot == -1 ? 100 : dot;
            separator = separator == -1 ? 100 : separator;

            let min = Math.min(space, dot, separator);
            selector = this.replaceID(selector.slice(0, index + min) +
                            '"]' + selector.slice(index + min));

        } else 
            selector = selector + '"]';
    }

    return selector;
}


const HTMLParsing = (htmlText, customClasses) => {
    let html = htmlText.replace(/ id=/gi, " data-id=");  // CSSReplaceId
    let [title, ind1, ind2] = ["", -1, -1]

    // Title parsing
    if (~html.indexOf('<title>')) {
        let ind1 = html.indexOf('<title>');
        let ind2 = html.indexOf('</title>', ind1);
        if (~ind2) {
            let user_title = html.slice(ind1+7, ind2);
            if (user_title.length)
                title = user_title;
        }
    }

    // Body parsing
    ind1 = html.indexOf('<body');
    ind2 = html.indexOf('</body>');
    if (~ind1) {
        if (~ind2)
            html = html.slice(html.indexOf('>', ind1)+1, ind2);
        else
            html = html.slice(html.indexOf('>', ind1)+ 1);
    }

    return [html, title]
}


const JSUnFreezeCycles = (code) => {
    // Спасатель от бесконечного цикла пользователя. MyObject - custom object
    let patterns = ['while', 'for']
    for (let i = 0; i < 2; i++) {
        let startIndex = 0;
        let index, lateIndex;

        do {
            index = code.indexOf(patterns[i], startIndex);
            lateIndex = code.indexOf(')', index);
            if (!~lateIndex || !~index) break;

            if ((index == 0
                    && patterns[i] == "while"
                    && code.length > index+6
                    && (code[index+5] == " "
                        || code[index+5] == "("
                        || code[index+5] == "\n"
                        || code[index+5] == "\t"))
                ||
                (index == 0
                    && patterns[i] == "for"
                    && code.length > index+4
                    && (code[index+3] == " "
                        || code[index+3] == "("
                        || code[index+3] == "\n"
                        || code[index+3] == "\t"))
                || 
                (index > 0
                    && patterns[i] == "while"
                    && (code[index-1] == " "
                        || code[index-1] == ";"
                        || code[index-1] == "\n"
                        || code[index-1] == "\t")
                    && (code[index+5] == " "
                        || code[index+5] == "("
                        || code[index+5] == "\n"
                        || code[index+5] == "\t"))
                ||
                (index > 0
                    && patterns[i] == "for"
                    && (code[index-1] == " "
                        || code[index-1] == ";"
                        || code[index-1] == "\n"
                        || code[index-1] == "\t")
                    && (code[index+3] == " "
                        || code[index+3] == "("
                        || code[index+3] == "\n"
                        || code[index+3] == "\t")))
            {
                let varName = "_tmrunfrzcycle" + index;
                lateIndex += 20 + varName.length;
                let tempIndex = lateIndex + 1;
                code = code.slice(0, index) + " var " + varName
                        + " = Date.now(); " + code.slice(index);

                let letter = " ";
                while (letter == " " || letter == "\n" || letter == "\t") {
                    if (code.length < lateIndex + 2)
                        break;
                    letter = code[lateIndex+1];
                    lateIndex++;
                }

                if (letter == " " || letter == "\n" || letter == "\t") {
                    startIndex = lateIndex;
                    break;
                }

                if (letter == "{") {
                    code = code.slice(0, lateIndex+1) + "if(Date.now()-"
                            + varName + ">200){MyObject.log.push('Timeo"
                            + "ut error');setTimeout(()=>{MyObject.prin"
                            + "tLog('error')},4);break;};"
                            + code.slice(lateIndex+1);
                    startIndex = tempIndex+120;
                } else {
                    let endIndex = code.indexOf(";", lateIndex);
                    if (!~endIndex) {
                        code = code.slice(0, tempIndex) + "{ break; }"
                                + code.slice(tempIndex);
                        startIndex = lateIndex;
                        break;
                    }
                    code = code.slice(0, tempIndex) + "{if (Date.now() - "
                            + varName + " > 200){MyObject.log.push('Timeo"
                            + "ut error');setTimeout(()=>{MyObject.printL"
                            + "og('error')},4);break;};"
                            + code.slice(tempIndex, endIndex+1) + "}"
                            + code.slice(endIndex+1);
                    startIndex = tempIndex + 120;
                }

            } else {
                if (code.length > index + 4)
                    startIndex = index + 3;
                else
                    break;
            }
        } while(~index)

    }
    return code;
}
