# # #single inheritance
# # class employee:
# #     def __init__(self,name,salalry):
# #         self.name = name
# #         self.salary = salalry
# #
# # amal = employee("amal",25000)
# # rohan = employee("rohan",15000)
# # class hr(employee):
# #     def __init__(self,name,salalry,roll):
# #         self.name = name
# #         self.salary = salalry
# #         self.roll = roll
# #
# #
# #
# #     def programmer(self):
# #         return f"name of programer {self.name},{self.roll}"
# #     print(amal.name)
# #     leave = 9
# #
# # arun = hr("rohan",15000,"hr")
# # print(arun.programmer())
# #
#
#
# # multiple inheritnce
#
#
# class employee:
#     def __init__(self,name,salalry):
#         self.name = name
#         self.salary = salalry
#
#
# class player:
#     no_game = 5
#     def __init__(self, name,game):
#         self.name = name
#         self.game = game
#
#     def print_details(self):
#         return f"the name of the player is {self.name}, the game he played is {self.game}"
#
# class coolprogrammer(employee, player):
#     pass
#
# amal = employee("amal",25000)
# rohan = employee("rohan",15000)
# anu = player("anagha","football")
# rajani = coolprogrammer("rajani",80000)
#
# deot = rajani.print_details()
# print(dot)


#multylevel inheritance

class dad:
    baseketball = 1
class son(dad):
    dance =1
    def isdance(self):
        return f"i dance {self.dance} time "

class grandson(son):

    dance = 6

    # def isdance(self):
    #     return f"hey jakson "\
    #         f"i dance  {self.dance} time very  awwesomly"


darry = dad()
larry = son()
harry = grandson()

print(harry.isdance())

print(harry.baseketball)