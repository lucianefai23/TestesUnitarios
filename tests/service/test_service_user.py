from src.service.service_user import ServiceUser


class TestServiceUser:

    def test_add_user_success(self):
        name_add = 'Luciane Santos'
        job_add = 'TechLead'
        wait_result = 'User added successfully'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert wait_result == result

