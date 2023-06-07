using System.Data;
using System.Data.SqlClient;     // 코드 추가

namespace CRUDApp
{
    public partial class Form1 : Form
    {
        string strConnect = "Server = mysqlserver-111.database.windows.net; database = BookStore; uid = devastra; pwd = **********;";    // 연결 문자열
        public Form1()
        {
            InitializeComponent();
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void btnSearch_Click(object sender, EventArgs e)
        {
            // 코드 추가하기 (1)
            SqlConnection DBConn = new SqlConnection();
            DBConn.ConnectionString = strConnect;       // 연결 문자열
            DBConn.Open();

            if (DBConn.State == System.Data.ConnectionState.Open)
            {
                MessageBox.Show("연결되었습니다.");
            }

            // 코드 추가하기 (2)
            string strQuery = "SELECT * FROM member";

            // 코드 추가하기 (4)
            if (txtboxSearchName.Text.Length > 0)
            {
                strQuery = string.Format("Select * FROM member WHERE Names = '{0}'", txtboxSearchName.Text);
            }

            ////  디버그 모드로 데이터가 불러와졌는지 확인해보기
            SqlCommand cmd = new SqlCommand();
            cmd.Connection = DBConn;

            // cmd.CommandText = strQuery;
            // SqlDataReader dr = cmd.ExecuteReader();

            // 코드 추가 하기 (3)
            SqlDataAdapter adapter = new SqlDataAdapter(strQuery, DBConn);

            DataSet ds = new DataSet();
            adapter.Fill(ds);

            dataGridView1.DataSource = ds.Tables[0];

            DBConn.Close();
        }

        private void dataGridView1_CellContentDoubleClick(object sender, DataGridViewCellEventArgs e)
        {
            txtboxSearchName.Text = dataGridView1.Rows[e.RowIndex].Cells[1].Value.ToString();
        }

        private void btnAdd_Click(object sender, EventArgs e)
        {
            string strQuery = string.Format("INSERT INTO member(Names, Addr, Mobile, Email) VALUES('{0}', '{1}', '{2}', '{3}')", txtboxName.Text, txtboxAddr.Text, txtboxMobile.Text, txtboxEmail.Text);

            // SqlConnection : 데이터베이스 서버와의 연결을 담당
            SqlConnection DBConn = new SqlConnection();

            DBConn.ConnectionString = strConnect;
            DBConn.Open();

            // SqlCommand : 데이터베이스 서버에서 실행될 SQL문 전달을 담당.
            SqlCommand cmd = new SqlCommand();

            cmd.Connection = DBConn;
            cmd.CommandText = strQuery;

            SqlDataReader rdr = cmd.ExecuteReader(); // DB에 바로 쿼리

            DBConn.Close();
        }

        private void btnDel_Click(object sender, EventArgs e)
        {
            string strQuery = string.Format("DELETE FROM member WHERE Names = '{0}'", txtboxDel.Text);

            //SqlConnection : 데이터베이스 서버와의 연결을 담당
            SqlConnection DBConn = new SqlConnection();

            DBConn.ConnectionString = strConnect;
            DBConn.Open();

            //SqlCommand : 데이터베이스 서버에서 실행될 SQL문 전달을 담당.
            SqlCommand cmd = new SqlCommand();

            cmd.Connection = DBConn;
            cmd.CommandText = strQuery;

            SqlDataReader rdr = cmd.ExecuteReader(); // DB에 바로 쿼리

            DBConn.Close();
        }

        private void btnUpdate_Click(object sender, EventArgs e)
        {
            string strQuery = string.Format("UPDATE member SET Names = '{0}' WHERE Names = '{1}'", txtboxNewName.Text, txtboxOldName.Text);

            SqlConnection DBConn = new SqlConnection();

            DBConn.ConnectionString = strConnect;
            DBConn.Open();

            SqlCommand cmd = new SqlCommand();

            cmd.Connection = DBConn;
            cmd.CommandText = strQuery;

            SqlDataReader rdr = cmd.ExecuteReader();     // DB에 바로 쿼리

            DBConn.Close();
        }
    }
}