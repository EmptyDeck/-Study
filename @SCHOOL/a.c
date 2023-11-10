

#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

uint8_t numbers[] = {0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x27, 0x7F, 0x67};
volatile uint16_t seconds = 0;
volatile uint8_t ms = 0;

ISR(TIMER3_COMPA_vect)
{
    ms++;
    if (ms == 10)
    {
        ms = 0;
        seconds++;
        if (seconds == 1000)
        {
            seconds = 0;
            ms = 0;
        }
    }
}

int main(void)
{
    UART0_init();

    DDRC = 0xff;
    DDRG = 0x0f;

    TCCR3B |= (1 << CS32) | (1 << WGM32);
    OCR3A = 6249;
    ETIMSK |= (1 << OCIE3A);
    sei();

    while (1)
    {
        PORTC = numbers[seconds / 100];
        PORTG = 0x08;
        _delay_ms(1);
        PORTC = numbers[(seconds % 100) / 10];
        PORTG = 0x04;
        _delay_ms(1);
        PORTC = numbers[(seconds % 10)] | 0x80;
        PORTG = 0x02;
        _delay_ms(1);
        PORTC = numbers[ms];
        PORTG = 0x01;
        _delay_ms(1);
    }
}