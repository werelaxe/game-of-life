from open_gl import variables_init, opengl_init, run_main_loop
from field import Field


def main():
    variables_init()
    opengl_init()

    run_main_loop()


if __name__ == '__main__':
    main()

    f = Field(2, 5, (3, 2))
    f.update()


