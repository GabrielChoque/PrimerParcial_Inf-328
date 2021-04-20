using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1 {
    public class Class1 {
        public Boolean isOp(string res) {
            string op = "+-*/";
            if (res != "" && op.Contains(res))
            {
                return true;
            }
                
            return false;
        }
        public int pri(string res) {
            string p = "+-";
            if (p.Contains(res))
            {
                return 0;
            }
               
            return 1;
        }
        public Boolean isNum(string res) {
            string num = "0123456789.";
            if (res != "" && num.Contains(res))
            {
                return true;
            }
   
            return false;
        }

        public string calc(string op, string num1, string num2) {
            double n1 = Double.Parse(num1.Replace(".", ","));
            double n2 = Double.Parse(num2.Replace(".", ","));
            if (op == "+")
            {
                return (n1 + n2).ToString().Replace(",", ".");
            }

            if (op == "-")
            {
                return (n1 - n2).ToString().Replace(",", ".");
            }

            if (op == "*")
            {
                return (n1 * n2).ToString().Replace(",", ".");
            }
                
 
            return (n1 / n2).ToString().Replace(",", ".");
        }

        public string Infix(string exp) {
            List<string> expr = new List<string>();
            foreach (char x in exp) {
                expr.Add(x + "");
            }
               
            List<string> pilaC = new List<string>();
            List<string> pilaN = new List<string>();
            pilaN.Add("0");
            string num = "", num2, num1, res, d, top, op;
            while (expr.Count() > 0) 
            {
                res = expr[0];
                expr.RemoveAt(0);
                if (expr.Count() > 0) {
                    d = expr[0];
                } else {
                    d = "";
                }
                if (isNum(res)== true) {
                    num += res;
                    if (!isNum(d)) {
                        pilaN.Add(num);
                        num = "";
                    }
                } else {
                    if (isOp(res)) 
                    {
                        while (true)
                        {
                            if (pilaC.Count() > 0)
                            {
                                top = pilaC[pilaC.Count() - 1];
                            } else 
                            {
                                top = "";
                            }
                            if (isOp(top)) 
                            {
                                if (!(pri(res) > pri(top))) 
                                {
                                    num2 = pilaN[pilaN.Count() - 1];
                                    pilaN.RemoveAt(pilaN.Count() - 1);
                                    op = pilaC[pilaC.Count() - 1];
                                    pilaC.RemoveAt(pilaC.Count() - 1);
                                    num1 = pilaN[pilaN.Count() - 1];
                                    pilaN.RemoveAt(pilaN.Count() - 1);
                                    pilaN.Add(calc(op, num1, num2));
                                } else 
                                {
                                    pilaC.Add(res);
                                    break;
                                }
                            } else 
                            {
                                pilaC.Add(res);
                                break;
                            }
                        }
                    } else 
                    {
                        if (res == "(") 
                        {
                            pilaC.Add(res);
                        } else {
                            if (res == ")") 
                            {
                                while (pilaC.Count() > 0)
                                {
                                    res = pilaC[pilaC.Count() - 1];
                                    pilaC.RemoveAt(pilaC.Count() - 1);
                                    if (res == "(") 
                                    {
                                        break;
                                    } else 
                                    {
                                        if (isOp(res)) 
                                        {
                                            num2 = pilaN[pilaN.Count() - 1];
                                            pilaN.RemoveAt(pilaN.Count() - 1);
                                            num1 = pilaN[pilaN.Count() - 1];
                                            pilaN.RemoveAt(pilaN.Count() - 1);
                                            pilaN.Add(calc(res, num1, num2));
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            while (pilaC.Count() > 0)
            {
                res = pilaC[pilaC.Count() - 1];
                pilaC.RemoveAt(pilaC.Count() - 1);
                if (res == "("){
                    break;
                }
                   
                else {
                    if (isOp(res)== true) 
                    {
                        num2 = pilaN[pilaN.Count() - 1];
                        pilaN.RemoveAt(pilaN.Count() - 1);
                        num1 = pilaN[pilaN.Count() - 1];
                        pilaN.RemoveAt(pilaN.Count() - 1);
                        pilaN.Add(calc(res, num1, num2));
                    }
                }
            }
            string respuesta = pilaN[pilaN.Count() - 1];
            pilaN.RemoveAt(pilaN.Count() - 1);
            return respuesta;
        }
    }
}
