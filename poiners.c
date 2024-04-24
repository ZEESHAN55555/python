main()
{
    int a=10;
    int *b=&a;
   int **c=&b;
    int ***d=&c;
    int ****e=&d;
    printf("a=%d\n",a); #10
    printf("adress of a %x \n",&a);
    printf("b=%d\n",*b);
    printf("adress of b %x \n",&b);
    printf("c=%d\n",*c);
    printf("adress of c %x \n",&c);
    printf("d=%d\n",*d);
    printf("adress of d %x \n",&d);
    printf("e=%d\n",*e);
    printf("adress of e %x \n",&e);


    printf("%d",a);      #10
    printf("%d",**b);    #10
    printf("%d",***c);   #10
    printf("%d",****d);  #10
    printf("%d",*****e); #10

}


Back tracking algorithm which is done using pointers.
  1    2    3    4 
1 Q

2

3

4

