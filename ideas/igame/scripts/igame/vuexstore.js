var store = new Vuex.Store({
  state: {

    // Time
    ty: 2018,   // year
    ts: 11,     // month
    td: 30,     // day
    tw: 5,      // weekday
    th: 16,     // hour
    tm: 1,      // minute

    // Player common stats
    pcl: 88.8888888,        // lifetime
    pcd: [1990, 6, 17],     // birth date
    pcw: 88.8,              // weight, kg
    pch: 198,               // height, sm

    // Player woman stats
    pwb: 90,    // boobs
    pwl: 3,     // boobs label
    pww: 60,    // belly
    pwa: 90,    // ass

    // Player woman sex stats
    land: "village",

    // Quests
    questFlags: {},

  },

  mutations: {
    timeflow: (state, min) => {
        var minutes = state.iGameMinute + min;

        if (minutes > 59) {
            var hours = ~~(minutes / 60);
            state.iGameMinute = minutes - hours * 60;
            hours += state.iGameHour;

            if (hours > 23) {
                var days = ~~(hours / 24);
                state.iGameHour = hours - days * 24;
                state.iGameWeekday = (state.iGameWeekday + days) % 7;

                days += state.iGameDay;
                var year = state.iGameYear;
                var month = state.iGameMonth;
                var monthDays = [99, 31, 99, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
                var currentMonthDays;

                while (true) {
                    monthDays[2] = year % 4 ? 29 : 28;
                    currentMonthDays = monthDays[month];

                    if (days > currentMonthDays) {
                        days -= currentMonthDays;
                        month++;

                        if (month > 12) {
                            month = 1;
                            year++;
                        }

                    } else {
                        state.iGameDay = days;
                        break;
                    }
                }

                state.iGameDay = days;
                state.iGameMonth = month;
                state.iGameYear = year;

            } else {
                state.iGameHour = hours;
            }

        } else {
            state.iGameMinute = minutes;
        }
    },
  },

  actions: {
    timeflow: ({commit}, min) => commit('timeflow', min),

    autosave: (state) => igs(state.state),

    setland: () => {
        let s = document.createElement('script');
        s.src = "scripts/locations/village.js";
        console.log(s);
        document.body.removeChild(document.body.querySelector('script:last-of-type'));
        document.body.appendChild(s);
        setTimeout(() => { document.getElementById('land').innerHTML = village }, 10);
    }
  }
})
