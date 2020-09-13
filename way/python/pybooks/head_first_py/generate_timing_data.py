import athletemodel
import yate
import glob

data_files = glob.glob("coach/*.txt")
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response())
print(yate.include_header("Coach Pappa's List of Athletes"))
print(yate.start_form("generate_timing_data.py"))
print(yate.paragraph("Select an atrhlete from the list to work with:"))
for each_athlete in atrhletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select"))
print(yate.include_footer({"Home": "/index.html"}))