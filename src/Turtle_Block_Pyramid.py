import turtle as msLogo
# Set row value to 0
msLogo.speed(0)
row_value = 0
def move_to_row(num_blocks):
    x_value = -((num_blocks*50)/2)
    y_value = -200 + (50 * row_value)
    msLogo.penup()
    msLogo.setposition(x_value,y_value)
    msLogo.pendown()

# This function draw a row of blocks based on user value    
def draw_block_row(num_blocks):
    for i in range(num_blocks):
        for i in range(4):
            msLogo.forward(50)
            msLogo.left(90)
        msLogo.forward(50)
       
num_blocks=int(input("How many blocks on the bottom row? (8 or less): "))
for i in range(num_blocks):
    move_to_row(num_blocks)
    row_value = row_value + 1
    draw_block_row(num_blocks)
    num_blocks = num_blocks - 1