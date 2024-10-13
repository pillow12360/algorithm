#include <iostream>
void printHello(void) {
	std::cout << "Hello!" << std::endl;
}

int main()
{
	// static_assert(sizeof(int) != 4, "int is 4byte");

	std::cout << sizeof(int8_t) << std::endl;
	std::cout << sizeof(int64_t) << std::endl;
	printHello();

	return 0;
}

