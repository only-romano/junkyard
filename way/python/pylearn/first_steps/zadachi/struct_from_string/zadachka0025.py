#! Штука, которая из такой строчки делает такую структуру


def shtuka_kotoraya_sdelaet(shtuka):
    return {'text': shtuka.split()[1], 'children':
    [shtuka_kotoraya_sdelaet(' '.join(shtuka.split()[2:-2]))]} if shtuka[0] == '<' and shtuka[-1] == '>' else []


print(shtuka_kotoraya_sdelaet('<\n    root1\n    <\n        fist1\n        <\n'
                        '            second1\n            <\n'
                        '                third1\n            >\n        >\n'
                        '        <\n             second2\n        >\n    >\n>'))




