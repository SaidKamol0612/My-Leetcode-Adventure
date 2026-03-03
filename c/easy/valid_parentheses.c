#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char *s);

int main(int argc, char const *argv[])
{
    // Testcase 1
    bool res = isValid("()");
    printf("%d %d\n", res, res);

    // Testcase 2
    res = isValid("()[]{}");
    printf("%d %d\n", res, res);

    // Testcase 3
    res = isValid("(]");
    printf("%d %d\n", res, !res);

    // Testcase 4
    res = isValid("([])");
    printf("%d %d\n", res, res);

    // Testcase 5
    res = isValid("([)]");
    printf("%d %d\n", res, !res);

    return 0;
}

bool isValid(char *s)
{
    int len = strlen(s);
    char stack[len];
    int top = -1;

    for (size_t i = 0; i < len; i++)
    {
        if (
            s[i] == '(' ||
            s[i] == '[' ||
            s[i] == '{')
            stack[++top] = s[i];
        else
        {
            if (top == -1)
                return false;

            char last = stack[top];
            if (
                (last == '(' && s[i] != ')') ||
                (last == '[' && s[i] != ']') ||
                (last == '{' && s[i] != '}'))
                return false;
            else
                stack[top--] = '\0';
        }
    }
    return top == -1;
}