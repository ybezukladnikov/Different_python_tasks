# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
# setattr(tb1, 'name', 'Франция')
# setattr(tb1, 'days', 6)
#
# TravelBlog.total_blogs +=1
#
# tb2 = TravelBlog()
# setattr(tb2, 'name', 'Италия')
# setattr(tb2, 'days', 5)
#
# TravelBlog.total_blogs +=1


class Figure:
    type_fig = 'ellipse'
    color = 'red'

    def __init__(self, start_pt, end_pt, color):
        self.start_pt = start_pt
        self.end_pt = end_pt
        self.color = color

fig1 = Figure((10, 5), (100, 20), 'blue')

del fig1.color

print(*fig1.__dict__)





