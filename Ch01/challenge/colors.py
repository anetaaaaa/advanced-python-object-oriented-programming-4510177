# %% Color database
color_db = {
    'red': 0xFF0000,
    'green': 0x00FF00,
    'blue': 0x0000FF,
}

class Colors:
    """Dynamically get color from color_db"""
    # my stupid solution
    def __init__(self, red = color_db['red'], green = color_db['green'], blue = color_db['blue']):
        self.green = green
        self.red = red
        self.blue = blue


# %% Test
colors = Colors()

val = colors.green
print(f'green: {val:06X}')  # 00FF00

# %%
