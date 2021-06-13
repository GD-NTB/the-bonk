/*
  Controls:
  'Space' - pause / resume
  'Left Click' - draw / erase cells (Only when paused)
  'Up Arrow' - increase speed
  'Down arrow' - decrease speed
*/

int screen_width = 75;           // Amount of cells (x), (int)
int screen_height = 75;          // Amount of cells (y), (int)

int cell_width = 10;              // Size of cells (x), (px)
int cell_height = 10;             // Size of cells (y), (px)

boolean randomise_cells = true;   // Initialise cells with random states (true/false)
int randomisation = 4;            // Chance that each cell is alive when randomised (100/r = %), (higher = less)

boolean playing = false;          // Initial playing condition (true/false)
int speed = 5;                    // Initial speed (int)

Cell[][] screen;
Cell[][] buffer;

int hover_tile_x = 0;
int hover_tile_y = 0;

int generation = 0;

int population()
{
  int pop = 0;
  for (int y = 0; y < screen_height; y++) {
    for (int x = 0; x < screen_width; x++) {
      if (screen[x][y].alive)
        pop++;
    }
  }
  return pop;
}

void set_title(){
  surface.setTitle("Conway's Game of Life (Generation: " + generation + ", population: " + population() + ", speed: " + speed + ")");
}

// Settings for sketch
void settings() {
  size(screen_width*cell_width, screen_height*cell_height);
}

// Key presses
void keyPressed()
{
  if (keyCode == UP)
    speed--;
  
  if (keyCode == DOWN)
    speed++;
  
  speed = constrain(speed, 1, 20);
  
  if (key == ' ')
    playing = !playing;
} 

// Executed before the first frame
void setup()
{  
  // No cell outline
  noStroke();

  screen = new Cell[screen_width][screen_height];

  // x, y, alive
  for (int y = 0; y < screen_height; y++) {
    for (int x = 0; x < screen_width; x++) {
      
      boolean alive = false;
      
      if (randomise_cells)
        alive = r_boolean();
       
      screen[x][y] = new Cell(x, y, alive);
    }
  }
  
  set_title();
}

// Executed every frame
void draw()
{
  // Hovered tile with mouse
  hover_tile_x = constrain(mouseX / cell_width, 0, screen_width-1);
  hover_tile_y = constrain(mouseY / cell_height, 0, screen_height-1);
  
  if (!playing && mousePressed) {
    if (mouseButton == LEFT)
      screen[hover_tile_x][hover_tile_y].alive = true;
    if (mouseButton == RIGHT)
      screen[hover_tile_x][hover_tile_y].alive = false;
  }
  
  if (frameCount % speed == 0 && playing)
    calculate();
  
  // Draw cells
  for (int y = 0; y < screen_height; y++) {
    for (int x = 0; x < screen_width; x++) {
      screen[x][y].draw();
    }
  }
  
  set_title();
}

// Calculate the current screen matrix
void calculate()
{
  generation++;
  
  /*
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
  */
  
  buffer = new Cell[screen_width][screen_height];
  
  // x, y, alive
  for (int y = 0; y < screen_height; y++) {
    for (int x = 0; x < screen_width; x++) {
      buffer[x][y] = new Cell(x, y, false);
    }
  }
      
  for (int y = 0; y < screen_height; y++) {
    for (int x = 0; x < screen_width; x++) {
      int neighbours = cell_neighbours(screen[x][y]);
      
      if ((screen[x][y].alive) && (neighbours < 2))
        buffer[x][y].alive = false;
        
      else if ((screen[x][y].alive) && (neighbours == 2 && neighbours == 3))
        buffer[x][y].alive = true;
        
      else if ((screen[x][y].alive) && (neighbours > 3))
        buffer[x][y].alive = false;
      
      else if ((!screen[x][y].alive) && (neighbours == 3))
        buffer[x][y].alive = true;
        
      else
        buffer[x][y].alive = screen[x][y].alive;
    }
  }
  
  screen = buffer;
}

int cell_neighbours(Cell cell)
{
  int x = cell.x;
  int y = cell.y;
  
  int neighbours = 0;

  for (int y_offset = -1; y_offset < 2; y_offset++) {
    for (int x_offset = -1; x_offset < 2; x_offset++) {
      
      int cx = x + x_offset; // current_cell_x
      int cy = y + y_offset; // current_cell_y
      
      // Out of bounds check
      if (screen_width > cx && cx >= 0 && screen_height > cy && cy >= 0)
      {
        if (screen[cx][cy].alive && screen[cx][cy] != cell)
          neighbours++;
      }
    }
  }
  
  return neighbours;
}

// Random boolean generator
boolean r_boolean()
{  
  if (floor(random(0, randomisation)) == 1)
    return true;
  else
    return false;
}

// Cell object
class Cell
{
  // Local
  int x, y;
  boolean alive;
  int id;

  Cell(int _x_, int _y_, boolean _alive_)
  {
    x = _x_;
    y = _y_;
    alive = _alive_;
  }

  // Draw this cell
  void draw()
  {
    if (alive)
      fill(255, 255, 255);
    else
      fill(0, 0, 0);

    rect(x*cell_width, y*cell_height, cell_width, cell_height);
  }
}
