from model_mvc import Person
import view_mvc

def showAll():
    #gets list of all Person objects
    people_in_db = Person.getAll()
    #print(people_in_db)
    #calls view
    return view_mvc.showAllView(people_in_db)

def start():
    view_mvc.startView()
    input_ = input()
    if input_ == 'y':
        return showAll() # Person.getAll()
    else:
        return view_mvc.endView()

if __name__ == "__main__": # if controller_mvc == controller_mvc: 
    #running controller function
    start()