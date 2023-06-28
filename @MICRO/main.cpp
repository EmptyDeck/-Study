// #define F_CPU 16000000UL
// #include <avr/io.h>
// #include <util/delay.h>

#include <stdio.h>

int main()
{
    printf("1");
    return 0;
}

/*
int main(void)
{
    DDRA = 0x07;
    while (1)
    {
        PORTA = 0x01;
        _delay_ms(1000);
        PORTA = 0x02;
        _delay_ms(1000);
        PORTA = 0x04;
        _delay_ms(1000);
    }
}
*/