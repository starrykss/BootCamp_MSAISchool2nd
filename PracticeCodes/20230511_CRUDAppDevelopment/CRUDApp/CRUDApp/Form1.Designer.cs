namespace CRUDApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridView1 = new DataGridView();
            btnSearch = new Button();
            name = new Label();
            txtboxSearchName = new TextBox();
            txtboxName = new TextBox();
            txtboxAddr = new TextBox();
            txtboxMobile = new TextBox();
            txtboxEmail = new TextBox();
            btnAdd = new Button();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            txtboxDel = new TextBox();
            label5 = new Label();
            btnDel = new Button();
            btnUpdate = new Button();
            txtboxOldName = new TextBox();
            txtboxNewName = new TextBox();
            label6 = new Label();
            label7 = new Label();
            ((System.ComponentModel.ISupportInitialize)dataGridView1).BeginInit();
            SuspendLayout();
            // 
            // dataGridView1
            // 
            dataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView1.Location = new Point(12, 12);
            dataGridView1.Name = "dataGridView1";
            dataGridView1.RowTemplate.Height = 25;
            dataGridView1.Size = new Size(609, 381);
            dataGridView1.TabIndex = 0;
            dataGridView1.CellContentDoubleClick += dataGridView1_CellContentDoubleClick;
            // 
            // btnSearch
            // 
            btnSearch.Location = new Point(640, 62);
            btnSearch.Name = "btnSearch";
            btnSearch.Size = new Size(148, 23);
            btnSearch.TabIndex = 1;
            btnSearch.Text = "검색";
            btnSearch.UseVisualStyleBackColor = true;
            btnSearch.Click += btnSearch_Click;
            // 
            // name
            // 
            name.AutoSize = true;
            name.Location = new Point(640, 35);
            name.Name = "name";
            name.Size = new Size(31, 15);
            name.TabIndex = 2;
            name.Text = "이름";
            // 
            // txtboxSearchName
            // 
            txtboxSearchName.Location = new Point(677, 32);
            txtboxSearchName.Name = "txtboxSearchName";
            txtboxSearchName.Size = new Size(111, 23);
            txtboxSearchName.TabIndex = 3;
            // 
            // txtboxName
            // 
            txtboxName.Location = new Point(12, 425);
            txtboxName.Name = "txtboxName";
            txtboxName.Size = new Size(103, 23);
            txtboxName.TabIndex = 4;
            // 
            // txtboxAddr
            // 
            txtboxAddr.Location = new Point(121, 425);
            txtboxAddr.Name = "txtboxAddr";
            txtboxAddr.Size = new Size(126, 23);
            txtboxAddr.TabIndex = 4;
            // 
            // txtboxMobile
            // 
            txtboxMobile.Location = new Point(253, 425);
            txtboxMobile.Name = "txtboxMobile";
            txtboxMobile.Size = new Size(134, 23);
            txtboxMobile.TabIndex = 4;
            // 
            // txtboxEmail
            // 
            txtboxEmail.Location = new Point(393, 425);
            txtboxEmail.Name = "txtboxEmail";
            txtboxEmail.Size = new Size(168, 23);
            txtboxEmail.TabIndex = 4;
            // 
            // btnAdd
            // 
            btnAdd.Location = new Point(567, 425);
            btnAdd.Name = "btnAdd";
            btnAdd.Size = new Size(75, 23);
            btnAdd.TabIndex = 5;
            btnAdd.Text = "추가";
            btnAdd.UseVisualStyleBackColor = true;
            btnAdd.Click += btnAdd_Click;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(50, 407);
            label1.Name = "label1";
            label1.Size = new Size(31, 15);
            label1.TabIndex = 6;
            label1.Text = "이름";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(171, 407);
            label2.Name = "label2";
            label2.Size = new Size(31, 15);
            label2.TabIndex = 7;
            label2.Text = "주소";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(298, 407);
            label3.Name = "label3";
            label3.Size = new Size(43, 15);
            label3.TabIndex = 8;
            label3.Text = "휴대폰";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(456, 407);
            label4.Name = "label4";
            label4.Size = new Size(43, 15);
            label4.TabIndex = 9;
            label4.Text = "이메일";
            // 
            // txtboxDel
            // 
            txtboxDel.Location = new Point(713, 395);
            txtboxDel.Name = "txtboxDel";
            txtboxDel.Size = new Size(75, 23);
            txtboxDel.TabIndex = 10;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(644, 398);
            label5.Name = "label5";
            label5.Size = new Size(63, 15);
            label5.TabIndex = 11;
            label5.Text = "삭제(이름)";
            // 
            // btnDel
            // 
            btnDel.Location = new Point(713, 424);
            btnDel.Name = "btnDel";
            btnDel.Size = new Size(75, 23);
            btnDel.TabIndex = 12;
            btnDel.Text = "삭제";
            btnDel.UseVisualStyleBackColor = true;
            btnDel.Click += btnDel_Click;
            // 
            // btnUpdate
            // 
            btnUpdate.Location = new Point(644, 344);
            btnUpdate.Name = "btnUpdate";
            btnUpdate.Size = new Size(144, 23);
            btnUpdate.TabIndex = 13;
            btnUpdate.Text = "업데이트";
            btnUpdate.UseVisualStyleBackColor = true;
            btnUpdate.Click += btnUpdate_Click;
            // 
            // txtboxOldName
            // 
            txtboxOldName.Location = new Point(713, 280);
            txtboxOldName.Name = "txtboxOldName";
            txtboxOldName.Size = new Size(71, 23);
            txtboxOldName.TabIndex = 14;
            // 
            // txtboxNewName
            // 
            txtboxNewName.Location = new Point(713, 315);
            txtboxNewName.Name = "txtboxNewName";
            txtboxNewName.Size = new Size(71, 23);
            txtboxNewName.TabIndex = 14;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(648, 283);
            label6.Name = "label6";
            label6.Size = new Size(59, 15);
            label6.TabIndex = 15;
            label6.Text = "바꿀 이름";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(636, 318);
            label7.Name = "label7";
            label7.Size = new Size(71, 15);
            label7.TabIndex = 16;
            label7.Text = "새로운 이름";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 459);
            Controls.Add(label7);
            Controls.Add(label6);
            Controls.Add(txtboxNewName);
            Controls.Add(txtboxOldName);
            Controls.Add(btnUpdate);
            Controls.Add(btnDel);
            Controls.Add(label5);
            Controls.Add(txtboxDel);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(btnAdd);
            Controls.Add(txtboxEmail);
            Controls.Add(txtboxMobile);
            Controls.Add(txtboxAddr);
            Controls.Add(txtboxName);
            Controls.Add(txtboxSearchName);
            Controls.Add(name);
            Controls.Add(btnSearch);
            Controls.Add(dataGridView1);
            Name = "Form1";
            Text = "간단한 CRUD 애플리케이션";
            ((System.ComponentModel.ISupportInitialize)dataGridView1).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private DataGridView dataGridView1;
        private Button btnSearch;
        private Label name;
        private TextBox txtboxSearchName;
        private TextBox txtboxName;
        private TextBox txtboxAddr;
        private TextBox txtboxMobile;
        private TextBox txtboxEmail;
        private Button btnAdd;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private TextBox txtboxDel;
        private Label label5;
        private Button btnDel;
        private Button btnUpdate;
        private TextBox txtboxOldName;
        private TextBox txtboxNewName;
        private Label label6;
        private Label label7;
    }
}