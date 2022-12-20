# public static Matriz operator * (Matriz mat1, Matriz mat2)
# {
#     if(mat1.Colunas != mat2.Linhas)
#         throw new Exception();

#     Matriz Result = new Matriz(mat1.Colunas,mat2.Linhas);

#     for ( int i=0; i<Result.Linhas; i++)
#     {
#         for(int j=0; j<Result.Colunas; j++)
#         {
#             int sum=0;
#             for (int k = 0; k < Result.Colunas; k++)
#             {
#                 sum += mat1.Valores[i,k] * mat2.Valores[k,j];
#             }
#             Result.Valores[i,j] = sum;
#         }
#     }
#     return Result;
# }

