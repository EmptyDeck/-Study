#define F_CPU 16000000UL
#include <avr/io.h>
#include <util/delay.h>
#include "UART0.h"
#include <string.h>
#include <stdio.h>
#include <avr/interrupt.h>

#define SpeedMotor1(s)	OCR1B = s
volatile unsigned int adc_value;

FILE OUTPUT
= FDEV_SETUP_STREAM(UART0_transmit, NULL, _FDEV_SETUP_WRITE);
FILE INPUT
= FDEV_SETUP_STREAM(NULL, UART0_receive, _FDEV_SETUP_READ);

void InitializeTimer1(void)
{
	TCCR1A |= (1<<WGM10);
	TCCR1B |= (1<<WGM12);
	TCCR1A |= (1<<COM1B1);
	TCCR1B |= (1<<CS11) | (1<<CS10);
	
	OCR1B = 0;
}

void ADC_init(unsigned char channel)
{
	ADMUX |= (1<<REFS0);
	ADCSRA |= 0x07;
	ADCSRA |= (1<<ADEN);
	ADCSRA |= (1<<ADFR);
	ADCSRA |= (1<<ADIE);
	
	ADMUX = ((ADMUX & 0xE0) | channel);
	ADCSRA |= (1<<ADSC);
	sei();
}

ISR(ADC_vect)
{
	adc_value = ADC;
}

int main(void)
{
	stdout = &OUTPUT;
	stdin = &INPUT;
	
	UART0_init();
	ADC_init(1);
	
	DDRB = 0xff;
	PORTB = 0x00;
	
	InitializeTimer1();
	
	while(1)
	{
		float input_volt = (adc_value * 5.0)/1024.0;
		printf("%f\r\n", input_volt);
		if(input_volt >= 3)
		{
			SpeedMotor1(255);
		}
		else
		{
			SpeedMotor1(0);
		}
		_delay_ms(500);
	}
	return 0;
}