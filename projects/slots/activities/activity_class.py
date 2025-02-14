# BASE ACTIVITY CLASS
class Activity:
    """
    Callable activity constructor
    usage
    activity = Activity(params)
    act1 = activity("Activity 1", *args, **kwargs)
    act2 = activity("Activity 2", *args, **kwargs)

    constructor returns list as:
    [name{str}, count{int}, last{bool} (, available{list}, sound_only{bool})]
    """
    # long is alias for "not last", short is alias for "last"
    def __init__(self, name=None, count=1, last=True, available=None, audio=False):
        self.name = name
        # count of unused activities
        self.count = count
        # last in line (if "True", next slot will not advice to continue)
        self.last = last
        # list of available video/audio
        self.available = available
        # if "True" - it is an audio, if "None" - it is audio-only basic activity
        self.audio = audio

    def __call__(self, *args, **kwargs):
        name, count, last, available = [None]*4
        # looking for unnamed args for a specific type
        for arg in args:
            if   isinstance(arg, str):
                name = arg
            elif isinstance(arg, bool):
                # fix-upped because isinstance(True, int) is True
                last = arg
            elif isinstance(arg, int):
                count = arg
            elif isinstance(arg, (list)):
                available = arg

        # order is - kwargs -> args -> default value, 'till first match
        name = 'name' in kwargs and kwargs['name'] or name or self.name
        count = 'count' in kwargs and kwargs['count'] or count or self.count

        if 'last' in kwargs:
            last = kwargs['last']
        elif 'long' in kwargs:
            last = not kwargs['long']
        elif 'short' in kwargs:
            last = kwargs['short']
        elif last == None:
            last = self.last

        result = [name, count, last]
        if not self.audio:
            # if not audio, adds availables param
            av_kwarg = 'available' in kwargs and kwargs['available']
            available = av_kwarg or available or self.available
            result.append(available)
            if self.audio == None:
                # flag for audio only basic activities
                # the "available" of this element consist of audio, not video
                result.append(True)

        return result


# exported value
__all__ = ['Activity']

if __name__ == '__main__':
    activity = Activity()
    print(activity("Activity 1"), activity("Activity 2"))
