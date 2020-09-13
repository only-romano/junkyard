# Buttons sets

main_buttons = [
    [["🔍 Поиск", "main_search_button"], ["⚙ Настройки", "main_settings_button"]],
    [["❤ Порно", "main_porn_button"]],
]


settings_buttons = [
    [["Мой пол", "-"]],
    [["👨 Мужской", "user_male"], ["👩 Женский", "user_female"]],
    [["Мой возраст", "-"]],
    [["18-22", "user_age_1822"], ["23-29", "user_age_2329"], ["30+", "user_age_30"]],
    [["Пол собеседника", "-"]],
    [["👨 Мужской", "pref_male"], ["👩 Женский", "pref_female"]],
    [["Возраст собеседника", "-"]],
    [["18-22", "pref_1822"], ["23-29", "pref_2329"], ["30+", "pref_30"]],
    [["Назад", "mainmenu"]]
]


user_default = {
    "sex": None,      #  None = no  |  "1" = male   |  "2" = female
    "age": None,      #  None = no  |  "1" = 18-22  |  "2" = 23-29  |  "3" = 30+
    "p_sex": None,     #  "0" = no   |  "1" = male   |  "2" = female  |  "12" = all 
    "p_age": None,     #  "0" = no   |  "1" = 18-22  |  "2" = 23-29   |  "3" = 30+
                      #  "12" = 18-22 + 23-29       |  "13" = 18-22 + 30+
                      #  "23" = 23-29 + 30+         |  "123" = all
    "ban": 0,         #  0 = no     |  1 = yes
    "msg_time": None, # 
    "partner": None,  #  chat_id of partner
}
