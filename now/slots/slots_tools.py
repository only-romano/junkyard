
def get_slot_params(slots, slot, index):
    return {
        'slot_time': slots.time(),
        'slot_index': index,
        'slot_type': str if isinstance(slot['activities'], str) else list,
        'has_video': slot['video'] is not None,
        'has_audio': slot['audio'] is not None,
        }

def basic(slot, params):
    if params['slot_type'] == str:
        choosen_basic = slot['activities']
        basic_index = None
        basic_a_ind = None
        run_next_b = False
    return {
        'choosen_basic': choosen_basic,
        'basic_index': basic_index,
        'basic_a_ind': basic_a_ind,
        'run_next_b': run_next_b,
        }

def update_slots(slots, p):
    if params['basic_index']:
        slots._slots[p['slot-index']]['activities'][p['basic_index']]['count'] -= 1
        if slots._slots[p['slot-index']]['activities'][p['basic_index']]['count'] == 0:
            slots._slots[p['slot-index']]['activities'][p['basic_index']] == None
        if params['basic_a_ind']:
            del slots._slots[params['slot-index']]['activities'][p['basic_index']]['available'][p['basic_a_ind']]

def video(slot, params):
    pass
def audio(slot, params):
    pass
def print_result(text):
    pass
