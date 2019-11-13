"""
Evening activities (until night siesta [included, 19:00 - 22:00])

 Now it consist of:
 - SLEEP slot
 - Evening meal slot
 - micro-activity slot
 - 4 standard slots
 - SLEEP slot
"""
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


# 1-st slot of module (31th at all) - current - SLEEP slot
slot_31 = ["СОН", None, None, 15]


# 2-nd slot of module (32th at all) - current - Evening meal slot
slot_32 = ["Ужин", None, "radiobroadcast", 15]


# 3-rd slot of module (33th at all) - current - micro-activity slot
slot_33 = AT.PLACEHOLDER


# 4-th slot of module (34th at all) - current - standard slot
slot_34 = AT.PLACEHOLDER


# 5-th slot of module (35th at all) - current - standard slot
slot_35 = AT.PLACEHOLDER


# 6-th slot of module (36th at all) - current - standard slot
slot_36 = AT.PLACEHOLDER


# 7-th slot of module (37th at all) - current - standard slot
slot_37 = AT.PLACEHOLDER


# 8-th slot of module (38th at all) - current - SLEEP slot
slot_38 = ["СОН", None, None, 15]


# exported variable
EVENING = [slot_31, slot_32, slot_33, slot_34, slot_35, slot_36, slot_37, slot_38]


__all__ = ["EVENING"]

if __name__ == '__main__':
    print(EVENING)
