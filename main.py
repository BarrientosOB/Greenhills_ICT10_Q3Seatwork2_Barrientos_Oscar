from pyscript import display, document


def check_cert(e):
    answer1 = document.getElementById('answer1').value
    answer2 = document.getElementById('answer2').value

    if answer1.lower() == "yes" and answer2.lower() == "yes":
        document.getElementById('output1').innerHTML = 'You are cleared for the intramurals!'
    else:
        document.getElementById('output1').innerHTML = 'Please complete the registration and obtain medical clearance first.'

def check_team(e):
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value

    document.getElementById('output').innerHTML = ''

    if section == "Emerald":
        document.getElementById('output').innerHTML = "<img src='yellow_tigers.png' height='150' width='150'> You are in the Yellow Tigers!"
    elif section == "Ruby":
        document.getElementById('output').innerHTML = "<img src='blue_bears.png' height='150' width='150'> You are in the Blue Bears!"
    elif section == "Sapphire":
        document.getElementById('output').innerHTML = "<img src='green_hornets.png' height='150' width='150'> You are in the Green Hornets!"
    elif section == "Topaz":
        document.getElementById('output').innerHTML = "<img src='red_bulldogs.png' height='150' width='150'> You are in the Red Bulldogs!"
    else:
        document.getElementById('output').innerHTML = 'Please select a valid section.'

