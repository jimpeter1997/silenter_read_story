#include <stdio.h>


int main(){
	int var_runoob = 10;
	int *p;
	p = &var_runoob;

	printf("var_runoob 变量的地址: %p \n", p);
	return 0;
}
