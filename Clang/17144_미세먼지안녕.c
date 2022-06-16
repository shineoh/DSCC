#include <stdio.h>

int R, C, T;
int lst[55][55];
int temp[55][55];
int cleaner_u=-1;

int di[4] = {1,0,0,-1};
int dj[4] = {0,1,-1,0};

void spread(){
  for(int i=0; i<R, i++;){
    for(int j=0; j<C, j++;){
      temp[i][j] = 0;
    }
  }
  for(int i=0; i<R, i++;){
    for(int j=0; j<C, j++;){
      int cnt = 0;
      if(lst[i][j]>0){
        for(int k=0; k<4, k++;){
          int ii = i+di[k];
          int jj = j+dj[k];
          if(0 <= ii && ii < R &&
            0 <= jj && jj < C &&
            lst[ii][jj] != -1){
              temp[ii][jj] += lst[i][j]/5;
              cnt += 1;
            }
        }
      }
      lst[i][j] -= (lst[i][j]/5)*cnt;
    }
  }
  for(int i=0; i<R, i++;){
    for(int j=0; j<C, j++;){
      lst[i][j] += temp[i][j];
    }
  }
}

void clean(){
  int i = cleaner_u-1, j=0;
  while(i>=0){
    lst[i][j] = lst[i-1][j];
    i--;
  }
  while(j<C-1){
    lst[i][j] = lst[i][j+1];
    j++;
  }
  while(i<cleaner_u){
    lst[i][j] = lst[i+1][j];
    i++;
  }
  while(j>1){
    lst[i][j] = lst[i][j+1];
    j--;
  }
  lst[i][j] = 0;

  i = cleaner_u+2;
  j=0;
  while(i<R-1){
        lst[i][j] = lst[i+1][j];
        i++;
    }
    while(j<C-1){
        lst[i][j] = lst[i][j+1];
        j++;
    }
    while(i>cleaner_u){
        lst[i][j] = lst[i-1][j];
        i--;
    }
    while(j>1){
        lst[i][j] = lst[i][j-1];
        j--;
    }
    lst[i][j]=0;
}



int main(){
  scanf("%d %d %d", &R, &C, &T);
  for(int i=0; i<R, i++;){
    for(int j=0; j<C, j++;){
      scanf("%d", &lst[i][j]);
      if(lst[i][j]==-1) cleaner_u=i;
    }
  }

  for(int t=0; t<T, t++;){
    spread();
    clean();
  }

  int ans = 2;
  for(int i=0; i<R, i++;){
    for(int j=0; j<C, j++;){
      ans += lst[i][j];
    }
  }
  printf("%d\n", ans);



}



