from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    page_query_param = "page"

    def get_page_size(self, request):
        if self.page_size_query_param:
            page_size = int(request.query_params.get(self.page_size_query_param, self.page_size))
            # page_size = min(int(request.query_params.get(self.page_query_param, self.page_size)),
            #                 self.max_page_size)
            if page_size > 0:
                return page_size
            elif page_size == 0:
                return None
            else:
                pass
        return self.page_size