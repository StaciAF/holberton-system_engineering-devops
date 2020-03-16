extern printf

	segment .data
	    msg db     "Hello, Holberton", 0x0
	    len equ     $ - msg
formatstr:
	              dd formatstring

	segment .rodata
formatstring:	 db 25H, 73H, 0AH, 00H


	segment .text
	    global  main

printstring:
	    push    dword [esp + 4]
	    push    dword [formatstr]
	    call    printf
	    add     esp, 8
	    ret

main:
	    enter 0,0
	    pusha
	    push msg
	    call printstring

	    popa
	    xor eax, eax
	    leave
	    ret
