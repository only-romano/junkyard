(function() {
    var bg1 = document.getElementById('start_bg1').style;
    var bg2 = document.getElementById('start_bg2').style;
    var gradientInterval;
    var stage = 0;

    var gradients = [
        "020111 60%,#20202c",
        "020111 10%,#3a3a52",
        "20202c 0%,#515175",
        "40405c 0%,#6f71aa 80%,#8a76ab",
        "4a4969 0%,#7072ab 50%,#cd82a0",
        "757abf 0%,#8583be 60%,#eab0d1",
        "82addb 0%,#ebb2b1",
        "94c5f8 1%,#a6e6ff 70%,#b1b5ea",
        "b7eaff 0%,#94dfff",
        "9be2fe 0%,#67d1fb",
        "90dffe 0%,#38a3d1",
        "57c1eb 0%,#246fa8",
        "2d91c2 0%,#1e528e",
        "2473ab 0%,#1e528e 70%,#5b7983",
        "1e528e 0%,#265889 50%,#9da671",
        "1e528e 0%,#728a7c 50%,#e9ce5d",
        "154277 0%,#576e71 30%,#e1c45e 70%,#b26339",
        "163C52 0%,#4F4F47 30%,#C5752D 60%,#B7490F 80%, #2F1107",
        "071B26 0%,#071B26 30%,#8A3B12 80%,#240E03",
        "010A10 30%,#59230B 80%,#2F1107",
        "090401 50%,#4B1D06",
        "00000c 80%,#150800",
    ];

    var changeBg = function() {

        if (stage % 2 === 0) {
            bg2.background = "linear-gradient(to bottom, #" + gradients[stage] + " 100%)";
            bg2.opacity = 1;
            bg1.opacity = 0;

        } else {
            bg1.background = "linear-gradient(to bottom, #" + gradients[stage] + " 100%)";
            bg1.opacity = 1;
            bg2.opacity = 0;

        }

        if (++stage === 22) {
            clearInterval(gradientInterval);
            bg2.transition = "opacity 5s";

            setTimeout((function() {
                bg2.opacity = 0;
                bg1.opacity = 0;
            }).bind(this), 100);

            return false;
        }
    }

    setTimeout((function () {
        gradientInterval = setInterval(changeBg.bind(this), 100);
    }).bind(this), 250);

})();