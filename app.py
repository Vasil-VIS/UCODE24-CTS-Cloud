from pathlib import Path
import os
from io import StringIO
# import pandas as pd
from viktor import ViktorController
from viktor.core import ViktorController, File, UserError, progress_message
from viktor.parametrization import ViktorParametrization, FileField, DownloadButton, Page, Text, LineBreak, ActionButton,NumberField
from viktor.result import DownloadResult
from viktor.views import ImageResult, ImageView, ImageAndDataView,ImageAndDataResult
from viktor.errors import UserError, InputViolation
from table import get_table
import io
import pandas as pd
from graph import get_graph


entity_folder_path =os.path.dirname(__file__)  # entity_type_a
ROOT = entity_folder_path


#Parametrization is used for user input (left side of the screen)
class Parametrization(ViktorParametrization):
    page_1 = Page('Cable Tension Calculator')
    page_1.field_1 = Text("""# Welcome to Cable Tension Calculator!""")
    page_1.field_2 = Text("""### This app is designed to automate calculating tension on big cables!""")
    page_1.lb1 = LineBreak()
    page_1.span = NumberField('1.Input the span lenght',flex=100,min=0)
    page_1.lb2 = LineBreak()
    page_1.weight = NumberField('2.Input the weight per unit lenght',flex=100,min=0)
    page_1.lb3 = LineBreak()
    page_1.cantenery = NumberField('3.Input the contenary constant',flex=100,min=0)
    page_1.lb4 = LineBreak()
    page_1.height = NumberField('4.Input the height lenght',flex=100,min=0)
    page_1.lb4 = LineBreak()
    page_1.download_btn = DownloadButton('Download Report',flex=30,longpoll=True, method='download_file')    


class Controller(ViktorController):
    label = 'My Entity Type'  # label of the entity type as seen by the user in the app's interface
    parametrization = Parametrization(width=33)  # parametrization associated with the editor of the Controller entity type
    viktor_enforce_field_constraints = True


    def download_file(self, params, **kwargs) ->DownloadResult:

        span=params.page_1.span
        weight=params.page_1.weight
        cantenery=params.page_1.cantenery
        height=params.page_1.height
        table = get_table(span,weight,cantenery,height)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer) as writer:
            table.to_excel(writer, sheet_name='Sheet1', index=True)

        xlsx_value = buffer.getvalue()

        graph = get_graph(table, cantenery, weight)

        return DownloadResult(File.from_data(xlsx_value), f'output.xlsx')


    # def get_user_manual(self, params, **kwargs):
    #     print(entity_folder_path)
    #     file_path = entity_folder_path + '/cable.pdf'
    #     return DownloadResult(file_content=File.from_path(file_path), file_name='cable.pdf')


    # @ImageAndDataView("Image View", duration_guess=1)
    # def get_image_data_view(self, params, **kwargs):
    #     span=params.page_1.span
    #     weight=params.page_1.weight
    #     cantenery=params.page_1.cantenery
    #     height=params.page_1.height
    #     violations = []
    #     violations.append(InputViolation("Input cannot be empty!", fields=['span', 'weight', 'cantenery','height']))
    #     if violations:
    #         raise UserError("Cannot calculate!", input_violations=violations)
        
    #     """
        
    #     PLOT
        
        
        
    #     """

    #     svg_data = StringIO()
    #     fig.savefig(svg_data, format='svg')
    #     plt.close()

    #     return ImageAndDataResult(svg_data, data_group)