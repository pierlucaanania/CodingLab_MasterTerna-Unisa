#include <stdio.h>

int main()

{

    int N,i,j,a[N],b[N];

    printf("How many elements? ");
    scanf("%d",&N);
    j = N-1;
    printf("Insert %d numbers: ", N);
        for (i = 0; i < N; i++)
            {scanf("%d", &a[i]);
            
            b[j] = a[i];
            j--;}
        
   for (i = 0; i < N; i++)
        printf("%d", b[i]);
    
    return 0;

}