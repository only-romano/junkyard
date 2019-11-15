from write_slots import load, write
from slots_tools import get_slot_params, basic, video, audio, update_slots, print_result

slots = load()
result = ""

index = 0
for slot in slots:
    print(slot)

print_result(result)
write(slots)
