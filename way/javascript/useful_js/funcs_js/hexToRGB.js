'use strict';

// HEX-to-RGB converter
const hexToRgb = (hex, opacity=1) => {
    let shortHandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
    hex = hex.replace(shortHandRegex, function(m, r, g, b) {
        return r + r + g + g + b + b;
    });

    let result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result   ? 'rgba(' + parseInt(result[1], 16) + ','
                              + parseInt(result[2], 16) + ','
                              + parseInt(result[3], 16) + ','
                              + opacity + ')'
                    : null;
}



// RGB-to-HEX Converter
const rgbToHex = (r,g,b) => "#"+((1<<24)+(r<<16)+(g<<8)+b).toString(16).slice(1);
