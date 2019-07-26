import mock









#封装mock   https://blog.csdn.net/iam_emily/article/details/82670540
def mock_test(mock_method,request_data,url,method,response_data):
	mock_method = mock.Mock(return_value=response_data)
	res = mock_method(url,method,request_data)
	return res
