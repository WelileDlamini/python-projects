#functions with outputs
def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f'{formated_f_name} {formated_l_name}'
formated_string = format_name('AnGelA', 'YU', )
print(formated_string)
