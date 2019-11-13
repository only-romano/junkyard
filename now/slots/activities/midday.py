"""
Midday activites (until second dinner [included, 13:00 - 15:30])

 Now it consist of:
 - 6 standard slots
"""
if __name__ == '__main__':
    import activity_templates as AT
else:
    import activities.activity_templates as AT


MIDDAY = AT.PLACEHOLDER

__all__ = ["MIDDAY"]

if __name__ == '__main__':
    print(MIDDAY)
