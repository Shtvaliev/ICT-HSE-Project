from data_import import FLIGHTS

from hist_graph import plotting as hist_plt
from scatter_graph import plotting as scat_plt
from box_graph import ploatting as box_plt
from anna_pivot import anna
from digit_standart import digit
from string_standart import stringg

hist_plt(FLIGHTS)
scat_plt(FLIGHTS)
box_plt(FLIGHTS)
anna()
import ivan_pivot
import shamil_pivot
import bar_flights
import bar_cityes
import pie_charts
digit(FLIGHTS, "код путешествия")
digit(FLIGHTS, "код пользователя")
digit(FLIGHTS, "цена")
digit(FLIGHTS, "время в пути")
digit(FLIGHTS, "дистанция")
stringg(FLIGHTS, "город вылета")
stringg(FLIGHTS, "город прилёта")
stringg(FLIGHTS, "класс")
stringg(FLIGHTS, "авиакомпания")
stringg(FLIGHTS, "дата")
import classic_graph