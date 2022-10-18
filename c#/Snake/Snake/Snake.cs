using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using System.Threading;

namespace MultiThreadingSnake
{
    public partial class Main : Form
    {
        int cols = 50, rows = 34, score = -1, HEAD = 0, TAIL = 0, nx = 0, ny = 0;   //columns, rows, score, initial mark, snake's end, next x, next y
        bool[,] bodyLocation;                                                       //store actual positions of all snake cell's
        bool gameOver = false, lockMoveThread;
        Cell[] snake = new Cell[1250];                                              //snake's body
        List<int> available = new List<int>();

        Random rand = new Random();
        System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
        initialScreen initialScreen;

        private static SemaphoreSlim foodSemaphore;

        public Main(initialScreen initial)
        { 
            InitializeComponent();
            GameStart();
            LaunchTimer();
            startThreads();
            initialScreen = initial;
        }

        //Initialize all variables
        private void GameStart()
        {
            bodyLocation = new bool[rows + 1, cols + 1];

            Cell head = new Cell((rand.Next() % cols) * 20, (rand.Next() % rows) * 20);

            foodSemaphore = new SemaphoreSlim(0, 1);
            foodSemaphore.Release();

            for (int i = 0; i < rows; i++)
                for (int j = 0; j < cols; j++)
                {
                    bodyLocation[i, j] = false;
                    available.Add(i * cols + j);
                }

            bodyLocation[(head.Location.Y / 20), (head.Location.X / 20)] = true;

            available.Remove(head.Location.Y / 20 * cols + head.Location.X / 20);
            snake[HEAD] = head;
            Controls.Add(head);
        }

        //Start timer to control game fps
        private void LaunchTimer()
        {
            timer.Interval = 100;
            timer.Tick += move;
            timer.Start();
        }

        //Declare and start threads
        private void startThreads()
        {
            Thread colliderCheckThread = new Thread(checkColliders)
            {
                Name = "Collider Checker"
            };
            colliderCheckThread.Start();

            Thread foodManagerThread = new Thread(foodManager)
            {
                Name = "Food Manager"
            };
            foodManagerThread.Start();
        }

        //Check if snake collides with itself or with the walls
        private void checkColliders()
        {
            int x, y;

            while (!gameOver)
            {
                x = snake[HEAD].Location.X;
                y = snake[HEAD].Location.Y;

                if (nx != 0 || ny != 0)
                {
                    DialogResult result = DialogResult.None;
                    if (crashBorder(nx + x, ny + y))
                    {
                        timer.Stop();
                        result = MessageBox.Show("Game Over");
                        gameOver = true;
                    }
                    else if (!lockMoveThread && itselfCrash((y + ny) / 20, (x + nx) / 20))
                    {
                        timer.Stop();
                        result = MessageBox.Show("Snake crashed his Body!");
                        gameOver = true;
                    }

                    if(result == DialogResult.OK)
                    {
                        closeGame();
                        
                    }

                }
                Thread.Sleep(100);
            }
        }

        //Check the foods in field and create new ones
        private void foodManager()
        {
            while (!gameOver)
            {
                foodSemaphore.Wait();
                newFoodLocation(FoodLabelRed);
                increaseScore();
            }
        }

        //Create a new food
        private void newFoodLocation(Label fdLabel)
        {
            available.Clear();

            for (int i = 0; i < rows; i++)

                for (int j = 0; j < cols; j++)

                    if (!bodyLocation[i, j]) available.Add(i * cols + j);

            int idx = rand.Next(available.Count) % available.Count;
            setFoodLocation(idx, fdLabel);
            
        }

        delegate void setFoodLocationCallback(int idx, Label fdLabel);
        private void setFoodLocation(int idx, Label fdLabel)
        {
            if (fdLabel.InvokeRequired)
            {
                setFoodLocationCallback set = new setFoodLocationCallback(setFoodLocation);
                FoodLabelRed.Invoke(set, new object[] { idx, fdLabel });
            }
            else
            {
                fdLabel.Left = (available[idx] * 20) % (cols * 20);

                fdLabel.Top = (available[idx] * 20) / (cols*20)* 20;
            }
            
        }

        private void increaseScore()
        {
            score += 1;
            setScoreValue(score);
        }

        delegate void setScoreValueCallback(int score);
        private void setScoreValue(int score)
        {
            if (this.ScoreLabel.InvokeRequired)
            {
                setScoreValueCallback set = new setScoreValueCallback(setScoreValue);
                this.Invoke(set, new object[] { score});

            }
            else
                ScoreLabel.Text = "Score: " + score.ToString();
        }
       
        //Snake's moviment
        private void move(object sender, EventArgs e)
        {
            if (nx == 0 && ny == 0) return;

            int x = snake[HEAD].Location.X;
            int y = snake[HEAD].Location.Y;

            if (collectFood(nx + x, ny + y))
            {
                Cell head = new Cell(x + nx, y + ny);

                HEAD = (HEAD - 1 + 1250) % 1250;
                snake[HEAD] = head;

                bodyLocation[head.Location.Y / 20, head.Location.X / 20] = true;

                Controls.Add(head);

                foodSemaphore.Release();
            }

            else
            {
                lockMoveThread = true; 

                bodyLocation[snake[TAIL].Location.Y / 20, snake[TAIL].Location.X / 20] = false;

                HEAD = (HEAD - 1 + 1250) % 1250;
                snake[HEAD] = snake[TAIL];
                snake[HEAD].Location = new Point(x + nx, y + ny);
                TAIL = (TAIL - 1 + 1250) % 1250;

                bodyLocation[(y + ny) / 20, (x + nx) / 20] = true;

                lockMoveThread = false;
            }

        }

        //Check if crashed with itself
        private bool itselfCrash(int row, int col)
        {
            return (bodyLocation[row, col]);
        }

        //Check if food was collected
        private bool collectFood(int x, int y)
        {
            if (FoodLabelRed.Location.X == x && FoodLabelRed.Location.Y == y)
                return true;

            return false;
        }

        //Check if snake crashed with a wall
        private bool crashBorder(int x, int y)
        {
            if (x < 0 || x > 1000 || y < 0 || y > 660)
                return true;

            return false;
        }

        private void mainInput(object sender, KeyEventArgs key)
        {
            nx = ny = 0;
            switch (key.KeyCode)
            {
                case Keys.Right:
                    nx = 20;
                    break;
                case Keys.Left:
                    nx = -20;
                    break;
                case Keys.Up:
                    ny = -20;
                    break;
                case Keys.Down:
                    ny = 20;
                    break;
            }
        }

        delegate void closeGameCallback();
        private void closeGame()
        {
            if (this.InvokeRequired)
            {
                closeGameCallback set = new closeGameCallback(closeGame);
                this.Invoke(set, new object[] { });

            }
            else
            {
                this.Hide();
                initialScreen.Show();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Main_Load(object sender, EventArgs e)
        {

        }
    }
}
