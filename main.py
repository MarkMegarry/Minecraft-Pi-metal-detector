from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos = mc.player.getPos()
#getPos stores coordinates in a Vec3 object, rather than a vector
#Retrieve values with pos.x, pos.y, pos.z etc.
#Check 100 blocks directly below player (Change to more efficient number)
for y in range(int(pos.y),100):
    blockType = mc.getBlock(pos.x,y*-1,pos.z)
    #Diamond condition
    if blockType == 56:
        mc.postToChat("Diamond ore beneath you!")
    #Iron condition
    elif blockType == 15:
        mc.postToChat("Iron ore beneath you!")
    print(blockType)
print("Done!")

