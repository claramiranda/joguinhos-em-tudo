using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MultiThreadingSnake
{
    class Cell : Label
    {

        public Cell(int x, int y)
        {
            Location = new Point(x, y);
            Size = new Size(20, 20);
            BackColor = Color.Orange;
            Enabled = false;
            this.BringToFront();
        }
    }
}
