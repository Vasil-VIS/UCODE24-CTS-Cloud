import pandas as pd
from define_formulas import Computation

def generate_values(s, k, w, h):
    comp = Computation(s=s, k=k, h=h, w=w)
    return {
        'Xr': comp.xR,
        'XL': comp.xL,
        'Yr': comp.y_xR,
        'YL': comp.y_xL,
        'L_T': comp.L_T,
        'Vr': comp.V_R,
        'VL': comp.V_L,
        'Tr': comp.T_R,
        'TL': comp.T_L
    }

def get_table(span, weight ,cantenery, height):

    def generate_values_list(x):
        values = []

        for i in range(0, x + 1, 5):
            values.append(i)

        return values

    length = len(generate_values_list(height))

    df = pd.DataFrame({
        'h': generate_values_list(height),
        'Xr': [0] * length,
        'XL': [0] * length,
        'Yr': [0] * length,
        'YL': [0] * length,
        'L_T': [0] * length,
        'Vr': [0] * length,
        'VL': [0] * length,
        'Tr': [0] * length,
        'TL': [0] * length,
    })
    
    # Apply the calculation to each row
    for index, row in df.iterrows():
        values = generate_values(span, cantenery, weight, row['h'])

        df.at[index, 'Xr'] = values['Xr']
        df.at[index, 'XL'] = values['XL']
        df.at[index, 'Yr'] = values['Yr']
        df.at[index, 'YL'] = values['YL']
        df.at[index, 'L_T'] = values['L_T']
        df.at[index, 'Vr'] = values['Vr']
        df.at[index, 'VL'] = values['VL']
        df.at[index, 'Tr'] = values['Tr']
        df.at[index, 'TL'] = values['TL']

    df_transpose = df.T

    # print(df_transpose)
    return df_transpose