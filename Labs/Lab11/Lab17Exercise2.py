class Member:
    def __init__(self, fname="", sname="", member_id=0, address="", cost=0, weight=0, max_lift=0):
        self.fname = fname
        self.sname = sname
        self.member_id = member_id
        self.address = address
        self.cost = cost
        self.weight = weight
        self.max_lift = max_lift

    def __str__(self):
        return_str = "Firstname: {}\nSurname: {}".format(self.fname,  self.sname)
        if self.member_id > 0:
            return_str += "\nMember ID: {}".format(self.member_id)

        if self.address != "":
            return_str += "\nAddress: {}".format(self.address)

        if self.cost > 0:
            return_str += "\nCost: €{}".format(self.cost)

        if self.cost > 0:
            return_str += "\nWeight: {}kg".format(self.weight)
        return_str += "\n"
        return return_str

class Equipment:
    def __init__(self, machine_name="", machine_id=0, location="", cost=0, loaded_weight=0, member=Member()):
        self.machine_name = machine_name
        self.machine_id = machine_id
        self.location = location
        self.cost = cost
        self.loaded_weight = loaded_weight
        self.membername = member.fname
        self.lift = member.max_lift


    def __str__(self):
        return_str = "Machine name: {}".format(self.machine_name)
        if self.machine_id > 0:
            return_str += "\nMachine_ID: {}".format(self.machine_id)
        if self.location != "":
            return_str += "\nLocation: {}".format(self.location)

        if self.cost > 0:
            return_str += "\nCost: €{}".format(self.cost)

        if self.loaded_weight > 0:
            return_str += "\nWeight Loaded: {}kg\n".format(self.loaded_weight)

        if self.lift > 0:
            answer = self.can_you_lift()
            if answer == True:
                return_str += "{} can lift Weight Loaded \n".format(self.membername)
            else:
                return_str += "{} cannot lift Weight Loaded \n".format(self.membername)
        return_str += "\n"
        return return_str

    def can_you_lift(self):
        if self.lift >= self.loaded_weight:
            return True
        elif self.lift < self.loaded_weight:
            return False






#Main

#Member
#Member(fname, sname, member_id, address, cost, weight, max_lift)
me1 = Member("Jack", "Levins", 196735, "Drogheda, Ireland", 32.99, 90, 120)
print(me1)
arnold = Member("Arnold", "Schwarzenegger", 1, "Hall of Fame", .50, 108, 56)
print(arnold)


#Machine/Equipment
#Equipment(machine_name, machine_id, location, cost, machine_weight, member) # member is the instance of member using machine
machine1 = Equipment("Chest Press", 4, "Upstairs", 1400, 85, arnold)
print(machine1)

machine2 = Equipment("Cable Machine", 6, "Downstairs", 1955, 96, me1)
print(machine2)




