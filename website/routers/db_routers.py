


class OnlineRouter:
    route_app_labels = {'online'}
    
    def db_for_read(self,model, **hists):
        if model._meta.app_label in self.route_app_labels:
            return 'online_db'
        return None
    
    def db_for_write(self,model, **hists):
        if model._meta.app_label in self.route_app_labels:
            return 'online_db'
        return None
    

    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db=='online_db'
        return None