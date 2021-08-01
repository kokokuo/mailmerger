import pytest
from os.path import expanduser
from faker import Faker
from faker.providers import file
from logging import Logger
from unittest.mock import patch, Mock
from typing import Dict, List, Callable, Any
from mailmerge.domain.models.sources import EmailDraftReader
from mailmerge.infra.io.searchers import FilePathSearcher
from mailmerge.infra.excepts.codes import ErrorCodesInfo
from mailmerge.infra.excepts.types import FilePathNotFound
from mailmerge.infra.excepts.types import FileFormatError
from mailmerge.infra.excepts.types import FileContentNotExist
from tests.config import TestSheetConfig, TestParsinExcelSheetConfig


@pytest.fixture(scope="function")
def faker():
    faker = Faker()
    faker.add_provider(file)
    return faker


class TestEmailDraftReader(object):
    SEARCHER_PACKAGE_PATH = "mailmerge.domain.models.sources.draft.FilePathSearcher"

    def test_load_exist_draft_filepath(self, faker: Faker):
        # Arrange
        fake_filename = faker.file_name(extension="html")
        expected = expanduser("~") + "/" + fake_filename

        # Arrange module imported class
        StubFilePathSearcher = patch(self.SEARCHER_PACKAGE_PATH).start()
        StubFilePathSearcher.exist.return_value = True
        StubFilePathSearcher.fullpath.return_value = expected
        # Act
        draft_reader = EmailDraftReader("~/" + fake_filename)
        # Assert
        assert draft_reader.draftpath == expected

    def test_load_non_exist_draft_filepath(self, faker: Faker):
        # Arrange
        fake_filename = faker.file_name(extension="html")
        expected = ErrorCodesInfo.EMAIL_DRAFT_PATH_NOT_EXIST.name

        # Arrange module imported class
        StubFilePathSearcher = patch(self.SEARCHER_PACKAGE_PATH).start()
        StubFilePathSearcher.exist.return_value = False
        # Act
        with pytest.raises(FilePathNotFound) as errinfo:
            EmailDraftReader("~/" + fake_filename)
        # Assert
        assert errinfo.value.error_code == expected
