class Tables2Router(object):
    """
    A router to control all database operations on models in
    the tables application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on tables models to 'users'
        """
        if model._meta.app_label == 'tables':
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'tables':
            return 'users'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the 'tables' app only appears on the 'users' db
        """
        if db == 'users':
            return model._meta.app_label == 'tables'
        elif model._meta.app_label == 'tables':
            return False
        return None