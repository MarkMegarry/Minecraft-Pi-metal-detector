from mcpi.minecraft import Minecraft
#Execution time measurement
import time
start  = time.time()
#MCPi setup
mc=Minecraft.create()
pos = mc.player.getPos()
#getPos stores coordinates in a Vec3 object, rather than a vector
#Retrieve values with pos.x, pos.y, pos.z etc.
#Check blocks directly below player, stop at bedrock
for y in range(int(pos.y),-120, -1):
    blockType = mc.getBlock(pos.x,y,pos.z)
     #Barrier to entry, check next block if not target block
    if blockType == 15 or blockType == 56 or blockType == 7:
    
         #Iron condition
        if blockType == 15:
            mc.postToChat("Iron ore beneath you!")
        #Diamond condition
        elif blockType == 56:
            mc.postToChat("Diamond ore beneath you!")
        #Bedrock condition
        else:
            break
    print(blockType)
print("Done!")
#Print execution time
end = time.time()
print("Execution time:" + str(end-start))
