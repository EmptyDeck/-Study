// CPU 주파수를 정의합니다.
#define F_CPU 16000000UL

// 필요한 AVR 라이브러리를 포함합니다.
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    // LED 패턴을 저장할 변수를 초기화합니다.
    char pattern = 0x01;

    // 포트 A를 LED를 제어하기 위한 출력으로 설정하고 포트 E를 입력으로 설정합니다.
    DDRA = 0xFF;
    DDRE = 0x00;

    // 초기 LED 패턴으로 포트 A를 설정합니다.
    PORTA = pattern;

    // 주 루프
    while (1)
    {
        // 포트 E의 특정 비트가 원하는 값으로 설정되어 있는지 확인합니다.
        if ((PINE & 0x30) == 0x20)
        {
            // 5 밀리초 동안 지연합니다.
            _delay_ms(5);

            // 조건이 더 이상 충족되지 않을 때까지 대기합니다.
            while ((PINE & 0x30) == 0x20)
                ;

            // 추가 5 밀리초 동안 지연합니다.
            _delay_ms(5);

            // LED 패턴을 왼쪽으로 시프트합니다.
            pattern <<= 1;

            // 패턴이 0이 되면 0x01로 재설정합니다.
            if (pattern == 0x00)
                pattern = 0x01;

            // 새로운 LED 패턴으로 포트 A를 업데이트합니다.
            PORTA = pattern;
        }
    }

    return 0;
}

////// use from here

DDRA = 0xff;
DDRE = 0x00;

if ((PINE & 0x30) == 0x20)             // off on
    if ((PINE & 0x30) == 0x10)         // on off
        if ((PINE & 0x30) == 0x00)     // off
            if ((PINE & 0x30) == 0x30) // on on

                //

                // CTC
                //  오버플로 인터럽트를 사용하는 방법
                ISR(TIMER1_OVF_vect)
                {
                    state = !state;
                    if (state)
                        PORTA = 0xFF;
                    else
                        PORTA = 0x00;
                }

int main(void)
{
    DDRA = 0xFF;
    PORTC = 0x00;
    TCCR1B |= (1 << CS12); // 256

    TIMSK |= (1 << TOIE1);
    sei();
    while (1)
    {
    }
    return 0;
}

// No prescaling
TCCR1B |= (1 << CS10);

// Prescale by 8
TCCR1B |= (1 << CS11);

// Prescale by 64
TCCR1B |= (1 << CS10) | (1 << CS11);

// Prescale by 256 (이미 주어진 코드에 있습니다)
TCCR1B |= (1 << CS12);

// Prescale by 1024
TCCR1B |= (1 << CS10) | (1 << CS12);

// 비교일치 인터럽트
ISR(TIMER1_COMPA_vect)
{
    // 비교일치 시 실행할 코드
    // 예: PORTB를 토글
    PORTB ^= 0xFF;
}
int main(void)
{
    // I/O 설정 예: PORTB를 출력으로 설정
    DDRB = 0xFF;

    // 타이머 설정
    TCCR1B |= (1 << CS10);               // 0
    TCCR1B |= (1 << CS11);               // 8
    TCCR1B |= (1 << CS10) | (1 << CS11); // 64
    TCCR1B |= (1 << CS12);               // 256
    TCCR1B |= (1 << CS10) | (1 << CS12); // 1024

    TCCR1A = 0; // Normal mode

    // 비교일치 값 설정 (예: 50000)
    OCR1A = 50000;

    // 비교일치 인터럽트 활성화
    TIMSK |= (1 << OCIE1A);

    // 전역 인터럽트 활성화
    sei();

    while (1)
    {
        // 메인 루프 코드 (필요한 경우)
    }

    return 0;
}
int main(void)
{
    DDRA = 0xFF;
    PORTA = 0x00;
    TCCR1B |= (1 << WGM12) | (1 << CS12);
    OCR1A = 0x7FFF;
    TIMSK |= (1 << OCIE1A);
    sei();
    while (1)
    {
    }
    return 0;
}