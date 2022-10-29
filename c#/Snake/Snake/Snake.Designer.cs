
namespace MultiThreadingSnake
{
    partial class Main
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.ScoreLabel = new System.Windows.Forms.Label();
            this.FoodLabelRed = new System.Windows.Forms.Label();
            this.BackGround = new System.Windows.Forms.Label();
            this.FoodLabelGreen = new System.Windows.Forms.Label();
            this.FoodLabelBlue = new System.Windows.Forms.Label();
            this.FoodLabelOrange = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // ScoreLabel
            // 
            this.ScoreLabel.AutoSize = true;
            this.ScoreLabel.Font = new System.Drawing.Font("Microsoft PhagsPa", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ScoreLabel.Location = new System.Drawing.Point(12, 9);
            this.ScoreLabel.Name = "ScoreLabel";
            this.ScoreLabel.Size = new System.Drawing.Size(76, 24);
            this.ScoreLabel.TabIndex = 0;
            this.ScoreLabel.Text = "Score: 0";
            this.ScoreLabel.Click += new System.EventHandler(this.label1_Click);
            // 
            // FoodLabelRed
            // 
            this.FoodLabelRed.BackColor = System.Drawing.Color.Red;
            this.FoodLabelRed.Location = new System.Drawing.Point(353, 161);
            this.FoodLabelRed.Name = "FoodLabelRed";
            this.FoodLabelRed.Size = new System.Drawing.Size(20, 20);
            this.FoodLabelRed.TabIndex = 1;
            // 
            // BackGround
            // 
            this.BackGround.BackColor = System.Drawing.Color.Transparent;
            this.BackGround.Location = new System.Drawing.Point(0, 60);
            this.BackGround.Margin = new System.Windows.Forms.Padding(0, 0, 3, 0);
            this.BackGround.Name = "BackGround";
            this.BackGround.Size = new System.Drawing.Size(1000, 700);
            this.BackGround.TabIndex = 0;
            this.BackGround.Text = "label1";
            this.BackGround.Visible = false;
            // 
            // FoodLabelGreen
            // 
            this.FoodLabelGreen.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.FoodLabelGreen.Location = new System.Drawing.Point(548, 161);
            this.FoodLabelGreen.Name = "FoodLabelGreen";
            this.FoodLabelGreen.Size = new System.Drawing.Size(20, 20);
            this.FoodLabelGreen.TabIndex = 2;
            this.FoodLabelGreen.Visible = false;
            // 
            // FoodLabelBlue
            // 
            this.FoodLabelBlue.BackColor = System.Drawing.Color.Blue;
            this.FoodLabelBlue.Location = new System.Drawing.Point(454, 161);
            this.FoodLabelBlue.Name = "FoodLabelBlue";
            this.FoodLabelBlue.Size = new System.Drawing.Size(20, 20);
            this.FoodLabelBlue.TabIndex = 3;
            this.FoodLabelBlue.Visible = false;
            // 
            // FoodLabelOrange
            // 
            this.FoodLabelOrange.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0)))));
            this.FoodLabelOrange.Location = new System.Drawing.Point(650, 161);
            this.FoodLabelOrange.Name = "FoodLabelOrange";
            this.FoodLabelOrange.Size = new System.Drawing.Size(20, 20);
            this.FoodLabelOrange.TabIndex = 4;
            this.FoodLabelOrange.Visible = false;
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(96F, 96F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Dpi;
            this.ClientSize = new System.Drawing.Size(1024, 681);
            this.Controls.Add(this.FoodLabelOrange);
            this.Controls.Add(this.FoodLabelBlue);
            this.Controls.Add(this.FoodLabelGreen);
            this.Controls.Add(this.FoodLabelRed);
            this.Controls.Add(this.ScoreLabel);
            this.Controls.Add(this.BackGround);
            this.Font = new System.Drawing.Font("Microsoft PhagsPa", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.KeyPreview = true;
            this.Name = "Main";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "MultiThreadingSnake";
            this.Load += new System.EventHandler(this.Main_Load);
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.mainInput);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label ScoreLabel;
        public System.Windows.Forms.Label FoodLabelRed;
        private System.Windows.Forms.Label BackGround;
        public System.Windows.Forms.Label FoodLabelGreen;
        public System.Windows.Forms.Label FoodLabelBlue;
        public System.Windows.Forms.Label FoodLabelOrange;
    }
}

