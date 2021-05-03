#(?) Create a class named comment.
#(?) The Comment class should have properties named username, text, likes, dislikes.
#(?) 4 different comments were created and the loop content reviews were examined.

class Comment:
    def __init__(self, username, text, likes=0, dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment("emirhansirin", "good course")
c2 = Comment("ahmetsirin", "very good course",50,100)
c3 = Comment("hamdisirin", "bad course")
c4 = Comment("minesirin", "it was a super course",120)

Comments = [c1, c2, c3, c4]

for c in Comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")