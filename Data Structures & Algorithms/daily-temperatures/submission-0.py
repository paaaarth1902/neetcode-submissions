class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # daily temperatures analogy:
        # there is a room. we have array of dudes with humber in their tees 
        # [30,38,30,36,35,40,28]
        # first guy enters the room. he sits on first chair (there are chairs lined up in that room one after another with first chair at opposite end of this infinite room)
        # now second guy comes by door. the guy on first chair, sees this door dude and observed he has bigger teeth number. he asks him what his index number is and he leaves that room with that index number in mind.
        # the second dude now goes and sits on first chair. as 3rd dude is by door, he sees that this 3rd dude has tee number less. so he don't do anything. 3rd duded comes and sits on chair next to him. 4th dude comes and he has bigger tee number than the current closest dude (3rd in this case). 3rd guy gets up, asks this new guy his index number and leaves with index number in min. 4th guy also thinks same but he sees tee number is less so does nothing. This keeps on happening till last dude.
        # If someone doesn't find a dude with bigger tee, he leaves room at end with 0 index in his mind.

        stk = []
        resultList = [0] * len(temperatures)

        for i in range(len(temperatures)):

            while(stk and temperatures[i] > temperatures[stk[-1]]):
                idx = stk.pop()
                resultList[idx] = i - idx
            stk.append(i)

        return resultList