#include <iostream>

int main()
{
	// static_assert(sizeof(int) != 4, "int is 4byte");

	std::cout << sizeof(int8_t) << std::endl;
	std::cout << sizeof(int64_t) << std::endl;
	
	return 0;
}