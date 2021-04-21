using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            Response.Write("hola gabo");
            string nombre, apellido, tiempo_php,tiempo_java;
            nombre = Request.QueryString["nombre"];
            apellido = Request.QueryString["apellido"];
            tiempo_php = Request.QueryString["tiempo_php"];
            tiempo_java = Request.QueryString["tiempo_java"];
            Response.Write("<title>dato</title>");
            Response.Write("<h3>" + nombre + " " + apellido + "</h3>");
            Response.Write("<br> tiempo_php: " + tiempo_php);
            String timeNet = DateTime.Now.ToString("dd/MM/yyyy") + " " + DateTime.Now.ToLongTimeString();
            Response.Write("<br>tiempo_net: " + timeNet);
             Response.Write("<br>tiempo_java: " + tiempo_java);
            if (nombre != null && apellido != null && tiempo_php != null && timeNet != null)
            {
                nombre = nombre.Replace("*", " ");
                apellido = apellido.Replace("*", " ");
                tiempo_php = tiempo_php.Replace("*", " ");
                timeNet = timeNet.Replace("*", " ");
            }
            

        }
    }
}